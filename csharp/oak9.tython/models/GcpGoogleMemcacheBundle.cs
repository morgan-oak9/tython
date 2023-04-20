// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_google_memcache_bundle.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.GoogleMemcacheBundle {

  /// <summary>Holder for reflection information generated from gcp/gcp_google_memcache_bundle.proto</summary>
  public static partial class GcpGoogleMemcacheBundleReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_google_memcache_bundle.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpGoogleMemcacheBundleReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiRnY3AvZ2NwX2dvb2dsZV9tZW1jYWNoZV9idW5kbGUucHJvdG8SJm9hazku",
            "dHl0aG9uLmdjcC5nb29nbGVfbWVtY2FjaGVfYnVuZGxlGhNzaGFyZWQvc2hh",
            "cmVkLnByb3RvGhZnY3AvZ2NwX21lbWNhY2hlLnByb3RvIlcKDkdvb2dsZU1l",
            "bWNhY2hlEkUKEW1lbWNhY2hlX2luc3RhbmNlGAEgASgLMioub2FrOS50eXRo",
            "b24uZ2NwLm1lbWNhY2hlLk1lbWNhY2hlSW5zdGFuY2ViBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, global::Oak9.Tython.Gcp.Memcache.GcpMemcacheReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.GoogleMemcacheBundle.GoogleMemcache), global::Oak9.Tython.Gcp.GoogleMemcacheBundle.GoogleMemcache.Parser, new[]{ "MemcacheInstance" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GoogleMemcache : pb::IMessage<GoogleMemcache>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<GoogleMemcache> _parser = new pb::MessageParser<GoogleMemcache>(() => new GoogleMemcache());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<GoogleMemcache> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.GoogleMemcacheBundle.GcpGoogleMemcacheBundleReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleMemcache() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleMemcache(GoogleMemcache other) : this() {
      memcacheInstance_ = other.memcacheInstance_ != null ? other.memcacheInstance_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleMemcache Clone() {
      return new GoogleMemcache(this);
    }

    /// <summary>Field number for the "memcache_instance" field.</summary>
    public const int MemcacheInstanceFieldNumber = 1;
    private global::Oak9.Tython.Gcp.Memcache.MemcacheInstance memcacheInstance_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Memcache.MemcacheInstance MemcacheInstance {
      get { return memcacheInstance_; }
      set {
        memcacheInstance_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as GoogleMemcache);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(GoogleMemcache other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(MemcacheInstance, other.MemcacheInstance)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (memcacheInstance_ != null) hash ^= MemcacheInstance.GetHashCode();
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
      if (memcacheInstance_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(MemcacheInstance);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (memcacheInstance_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(MemcacheInstance);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (memcacheInstance_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(MemcacheInstance);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(GoogleMemcache other) {
      if (other == null) {
        return;
      }
      if (other.memcacheInstance_ != null) {
        if (memcacheInstance_ == null) {
          MemcacheInstance = new global::Oak9.Tython.Gcp.Memcache.MemcacheInstance();
        }
        MemcacheInstance.MergeFrom(other.MemcacheInstance);
      }
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
            if (memcacheInstance_ == null) {
              MemcacheInstance = new global::Oak9.Tython.Gcp.Memcache.MemcacheInstance();
            }
            input.ReadMessage(MemcacheInstance);
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
            if (memcacheInstance_ == null) {
              MemcacheInstance = new global::Oak9.Tython.Gcp.Memcache.MemcacheInstance();
            }
            input.ReadMessage(MemcacheInstance);
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
