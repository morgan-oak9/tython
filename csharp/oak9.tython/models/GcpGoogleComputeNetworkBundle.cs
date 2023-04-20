// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_google_compute_network_bundle.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.GoogleComputeNetworkBundle {

  /// <summary>Holder for reflection information generated from gcp/gcp_google_compute_network_bundle.proto</summary>
  public static partial class GcpGoogleComputeNetworkBundleReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_google_compute_network_bundle.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpGoogleComputeNetworkBundleReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CitnY3AvZ2NwX2dvb2dsZV9jb21wdXRlX25ldHdvcmtfYnVuZGxlLnByb3Rv",
            "Ei1vYWs5LnR5dGhvbi5nY3AuZ29vZ2xlX2NvbXB1dGVfbmV0d29ya19idW5k",
            "bGUaE3NoYXJlZC9zaGFyZWQucHJvdG8aHWdjcC9nY3BfY29tcHV0ZV9uZXR3",
            "b3JrLnByb3RvIqwCChRHb29nbGVDb21wdXRlTmV0d29yaxJICg9jb21wdXRl",
            "X25ldHdvcmsYASABKAsyLy5vYWs5LnR5dGhvbi5nY3AuY29tcHV0ZV9uZXR3",
            "b3JrLkNvbXB1dGVOZXR3b3JrElcKF2NvbXB1dGVfbmV0d29ya19wZWVyaW5n",
            "GAIgAygLMjYub2FrOS50eXRob24uZ2NwLmNvbXB1dGVfbmV0d29yay5Db21w",
            "dXRlTmV0d29ya1BlZXJpbmcScQolY29tcHV0ZV9uZXR3b3JrX3BlZXJpbmdf",
            "cm91dGVzX2NvbmZpZxgDIAMoCzJCLm9hazkudHl0aG9uLmdjcC5jb21wdXRl",
            "X25ldHdvcmsuQ29tcHV0ZU5ldHdvcmtQZWVyaW5nUm91dGVzQ29uZmlnYgZw",
            "cm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, global::Oak9.Tython.Gcp.ComputeNetwork.GcpComputeNetworkReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.GoogleComputeNetworkBundle.GoogleComputeNetwork), global::Oak9.Tython.Gcp.GoogleComputeNetworkBundle.GoogleComputeNetwork.Parser, new[]{ "ComputeNetwork", "ComputeNetworkPeering", "ComputeNetworkPeeringRoutesConfig" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GoogleComputeNetwork : pb::IMessage<GoogleComputeNetwork>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<GoogleComputeNetwork> _parser = new pb::MessageParser<GoogleComputeNetwork>(() => new GoogleComputeNetwork());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<GoogleComputeNetwork> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.GoogleComputeNetworkBundle.GcpGoogleComputeNetworkBundleReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleComputeNetwork() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleComputeNetwork(GoogleComputeNetwork other) : this() {
      computeNetwork_ = other.computeNetwork_ != null ? other.computeNetwork_.Clone() : null;
      computeNetworkPeering_ = other.computeNetworkPeering_.Clone();
      computeNetworkPeeringRoutesConfig_ = other.computeNetworkPeeringRoutesConfig_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleComputeNetwork Clone() {
      return new GoogleComputeNetwork(this);
    }

    /// <summary>Field number for the "compute_network" field.</summary>
    public const int ComputeNetworkFieldNumber = 1;
    private global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetwork computeNetwork_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetwork ComputeNetwork {
      get { return computeNetwork_; }
      set {
        computeNetwork_ = value;
      }
    }

    /// <summary>Field number for the "compute_network_peering" field.</summary>
    public const int ComputeNetworkPeeringFieldNumber = 2;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeering> _repeated_computeNetworkPeering_codec
        = pb::FieldCodec.ForMessage(18, global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeering.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeering> computeNetworkPeering_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeering>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeering> ComputeNetworkPeering {
      get { return computeNetworkPeering_; }
    }

    /// <summary>Field number for the "compute_network_peering_routes_config" field.</summary>
    public const int ComputeNetworkPeeringRoutesConfigFieldNumber = 3;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeeringRoutesConfig> _repeated_computeNetworkPeeringRoutesConfig_codec
        = pb::FieldCodec.ForMessage(26, global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeeringRoutesConfig.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeeringRoutesConfig> computeNetworkPeeringRoutesConfig_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeeringRoutesConfig>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetworkPeeringRoutesConfig> ComputeNetworkPeeringRoutesConfig {
      get { return computeNetworkPeeringRoutesConfig_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as GoogleComputeNetwork);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(GoogleComputeNetwork other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(ComputeNetwork, other.ComputeNetwork)) return false;
      if(!computeNetworkPeering_.Equals(other.computeNetworkPeering_)) return false;
      if(!computeNetworkPeeringRoutesConfig_.Equals(other.computeNetworkPeeringRoutesConfig_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (computeNetwork_ != null) hash ^= ComputeNetwork.GetHashCode();
      hash ^= computeNetworkPeering_.GetHashCode();
      hash ^= computeNetworkPeeringRoutesConfig_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (computeNetwork_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ComputeNetwork);
      }
      computeNetworkPeering_.WriteTo(output, _repeated_computeNetworkPeering_codec);
      computeNetworkPeeringRoutesConfig_.WriteTo(output, _repeated_computeNetworkPeeringRoutesConfig_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (computeNetwork_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ComputeNetwork);
      }
      computeNetworkPeering_.WriteTo(ref output, _repeated_computeNetworkPeering_codec);
      computeNetworkPeeringRoutesConfig_.WriteTo(ref output, _repeated_computeNetworkPeeringRoutesConfig_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (computeNetwork_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ComputeNetwork);
      }
      size += computeNetworkPeering_.CalculateSize(_repeated_computeNetworkPeering_codec);
      size += computeNetworkPeeringRoutesConfig_.CalculateSize(_repeated_computeNetworkPeeringRoutesConfig_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(GoogleComputeNetwork other) {
      if (other == null) {
        return;
      }
      if (other.computeNetwork_ != null) {
        if (computeNetwork_ == null) {
          ComputeNetwork = new global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetwork();
        }
        ComputeNetwork.MergeFrom(other.ComputeNetwork);
      }
      computeNetworkPeering_.Add(other.computeNetworkPeering_);
      computeNetworkPeeringRoutesConfig_.Add(other.computeNetworkPeeringRoutesConfig_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (computeNetwork_ == null) {
              ComputeNetwork = new global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetwork();
            }
            input.ReadMessage(ComputeNetwork);
            break;
          }
          case 18: {
            computeNetworkPeering_.AddEntriesFrom(input, _repeated_computeNetworkPeering_codec);
            break;
          }
          case 26: {
            computeNetworkPeeringRoutesConfig_.AddEntriesFrom(input, _repeated_computeNetworkPeeringRoutesConfig_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (computeNetwork_ == null) {
              ComputeNetwork = new global::Oak9.Tython.Gcp.ComputeNetwork.ComputeNetwork();
            }
            input.ReadMessage(ComputeNetwork);
            break;
          }
          case 18: {
            computeNetworkPeering_.AddEntriesFrom(ref input, _repeated_computeNetworkPeering_codec);
            break;
          }
          case 26: {
            computeNetworkPeeringRoutesConfig_.AddEntriesFrom(ref input, _repeated_computeNetworkPeeringRoutesConfig_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code