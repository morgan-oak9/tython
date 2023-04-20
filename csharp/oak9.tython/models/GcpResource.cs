// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_resource.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.Resource {

  /// <summary>Holder for reflection information generated from gcp/gcp_resource.proto</summary>
  public static partial class GcpResourceReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_resource.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpResourceReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChZnY3AvZ2NwX3Jlc291cmNlLnByb3RvEhhvYWs5LnR5dGhvbi5nY3AucmVz",
            "b3VyY2UaE3NoYXJlZC9zaGFyZWQucHJvdG8iPgocUmVzb3VyY2VNYW5hZ2Vy",
            "TGllblhUaW1lb3V0cxIOCgZjcmVhdGUYASABKAkSDgoGZGVsZXRlGAIgASgJ",
            "Io0CChNSZXNvdXJjZU1hbmFnZXJMaWVuEhMKC2NyZWF0ZV90aW1lGAEgASgJ",
            "EgoKAmlkGAIgASgJEgwKBG5hbWUYAyABKAkSDgoGb3JpZ2luGAQgASgJEg4K",
            "BnBhcmVudBgFIAEoCRIOCgZyZWFzb24YBiABKAkSFAoMcmVzdHJpY3Rpb25z",
            "GAcgAygJEkgKCHRpbWVvdXRzGAggASgLMjYub2FrOS50eXRob24uZ2NwLnJl",
            "c291cmNlLlJlc291cmNlTWFuYWdlckxpZW5YVGltZW91dHMSNwoNcmVzb3Vy",
            "Y2VfaW5mbxgJIAEoCzIgLm9hazkudHl0aG9uLnNoYXJlZC5SZXNvdXJjZUlu",
            "Zm9iBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.Resource.ResourceManagerLienXTimeouts), global::Oak9.Tython.Gcp.Resource.ResourceManagerLienXTimeouts.Parser, new[]{ "Create", "Delete" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.Resource.ResourceManagerLien), global::Oak9.Tython.Gcp.Resource.ResourceManagerLien.Parser, new[]{ "CreateTime", "Id", "Name", "Origin", "Parent", "Reason", "Restrictions", "Timeouts", "ResourceInfo" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class ResourceManagerLienXTimeouts : pb::IMessage<ResourceManagerLienXTimeouts>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ResourceManagerLienXTimeouts> _parser = new pb::MessageParser<ResourceManagerLienXTimeouts>(() => new ResourceManagerLienXTimeouts());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ResourceManagerLienXTimeouts> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.Resource.GcpResourceReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceManagerLienXTimeouts() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceManagerLienXTimeouts(ResourceManagerLienXTimeouts other) : this() {
      create_ = other.create_;
      delete_ = other.delete_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceManagerLienXTimeouts Clone() {
      return new ResourceManagerLienXTimeouts(this);
    }

    /// <summary>Field number for the "create" field.</summary>
    public const int CreateFieldNumber = 1;
    private string create_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Create {
      get { return create_; }
      set {
        create_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "delete" field.</summary>
    public const int DeleteFieldNumber = 2;
    private string delete_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Delete {
      get { return delete_; }
      set {
        delete_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ResourceManagerLienXTimeouts);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ResourceManagerLienXTimeouts other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Create != other.Create) return false;
      if (Delete != other.Delete) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Create.Length != 0) hash ^= Create.GetHashCode();
      if (Delete.Length != 0) hash ^= Delete.GetHashCode();
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
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
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
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
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
      if (Create.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Create);
      }
      if (Delete.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Delete);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ResourceManagerLienXTimeouts other) {
      if (other == null) {
        return;
      }
      if (other.Create.Length != 0) {
        Create = other.Create;
      }
      if (other.Delete.Length != 0) {
        Delete = other.Delete;
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
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
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
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class ResourceManagerLien : pb::IMessage<ResourceManagerLien>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ResourceManagerLien> _parser = new pb::MessageParser<ResourceManagerLien>(() => new ResourceManagerLien());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ResourceManagerLien> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.Resource.GcpResourceReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceManagerLien() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceManagerLien(ResourceManagerLien other) : this() {
      createTime_ = other.createTime_;
      id_ = other.id_;
      name_ = other.name_;
      origin_ = other.origin_;
      parent_ = other.parent_;
      reason_ = other.reason_;
      restrictions_ = other.restrictions_.Clone();
      timeouts_ = other.timeouts_ != null ? other.timeouts_.Clone() : null;
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceManagerLien Clone() {
      return new ResourceManagerLien(this);
    }

    /// <summary>Field number for the "create_time" field.</summary>
    public const int CreateTimeFieldNumber = 1;
    private string createTime_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string CreateTime {
      get { return createTime_; }
      set {
        createTime_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 2;
    private string id_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Id {
      get { return id_; }
      set {
        id_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 3;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "origin" field.</summary>
    public const int OriginFieldNumber = 4;
    private string origin_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Origin {
      get { return origin_; }
      set {
        origin_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "parent" field.</summary>
    public const int ParentFieldNumber = 5;
    private string parent_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Parent {
      get { return parent_; }
      set {
        parent_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "reason" field.</summary>
    public const int ReasonFieldNumber = 6;
    private string reason_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Reason {
      get { return reason_; }
      set {
        reason_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "restrictions" field.</summary>
    public const int RestrictionsFieldNumber = 7;
    private static readonly pb::FieldCodec<string> _repeated_restrictions_codec
        = pb::FieldCodec.ForString(58);
    private readonly pbc::RepeatedField<string> restrictions_ = new pbc::RepeatedField<string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<string> Restrictions {
      get { return restrictions_; }
    }

    /// <summary>Field number for the "timeouts" field.</summary>
    public const int TimeoutsFieldNumber = 8;
    private global::Oak9.Tython.Gcp.Resource.ResourceManagerLienXTimeouts timeouts_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Resource.ResourceManagerLienXTimeouts Timeouts {
      get { return timeouts_; }
      set {
        timeouts_ = value;
      }
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 9;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ResourceManagerLien);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ResourceManagerLien other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (CreateTime != other.CreateTime) return false;
      if (Id != other.Id) return false;
      if (Name != other.Name) return false;
      if (Origin != other.Origin) return false;
      if (Parent != other.Parent) return false;
      if (Reason != other.Reason) return false;
      if(!restrictions_.Equals(other.restrictions_)) return false;
      if (!object.Equals(Timeouts, other.Timeouts)) return false;
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (CreateTime.Length != 0) hash ^= CreateTime.GetHashCode();
      if (Id.Length != 0) hash ^= Id.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (Origin.Length != 0) hash ^= Origin.GetHashCode();
      if (Parent.Length != 0) hash ^= Parent.GetHashCode();
      if (Reason.Length != 0) hash ^= Reason.GetHashCode();
      hash ^= restrictions_.GetHashCode();
      if (timeouts_ != null) hash ^= Timeouts.GetHashCode();
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
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
      if (CreateTime.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(CreateTime);
      }
      if (Id.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Id);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Name);
      }
      if (Origin.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Origin);
      }
      if (Parent.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Parent);
      }
      if (Reason.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Reason);
      }
      restrictions_.WriteTo(output, _repeated_restrictions_codec);
      if (timeouts_ != null) {
        output.WriteRawTag(66);
        output.WriteMessage(Timeouts);
      }
      if (resourceInfo_ != null) {
        output.WriteRawTag(74);
        output.WriteMessage(ResourceInfo);
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
      if (CreateTime.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(CreateTime);
      }
      if (Id.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Id);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Name);
      }
      if (Origin.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Origin);
      }
      if (Parent.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Parent);
      }
      if (Reason.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Reason);
      }
      restrictions_.WriteTo(ref output, _repeated_restrictions_codec);
      if (timeouts_ != null) {
        output.WriteRawTag(66);
        output.WriteMessage(Timeouts);
      }
      if (resourceInfo_ != null) {
        output.WriteRawTag(74);
        output.WriteMessage(ResourceInfo);
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
      if (CreateTime.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(CreateTime);
      }
      if (Id.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Id);
      }
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (Origin.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Origin);
      }
      if (Parent.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Parent);
      }
      if (Reason.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Reason);
      }
      size += restrictions_.CalculateSize(_repeated_restrictions_codec);
      if (timeouts_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Timeouts);
      }
      if (resourceInfo_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ResourceManagerLien other) {
      if (other == null) {
        return;
      }
      if (other.CreateTime.Length != 0) {
        CreateTime = other.CreateTime;
      }
      if (other.Id.Length != 0) {
        Id = other.Id;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      if (other.Origin.Length != 0) {
        Origin = other.Origin;
      }
      if (other.Parent.Length != 0) {
        Parent = other.Parent;
      }
      if (other.Reason.Length != 0) {
        Reason = other.Reason;
      }
      restrictions_.Add(other.restrictions_);
      if (other.timeouts_ != null) {
        if (timeouts_ == null) {
          Timeouts = new global::Oak9.Tython.Gcp.Resource.ResourceManagerLienXTimeouts();
        }
        Timeouts.MergeFrom(other.Timeouts);
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
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
            CreateTime = input.ReadString();
            break;
          }
          case 18: {
            Id = input.ReadString();
            break;
          }
          case 26: {
            Name = input.ReadString();
            break;
          }
          case 34: {
            Origin = input.ReadString();
            break;
          }
          case 42: {
            Parent = input.ReadString();
            break;
          }
          case 50: {
            Reason = input.ReadString();
            break;
          }
          case 58: {
            restrictions_.AddEntriesFrom(input, _repeated_restrictions_codec);
            break;
          }
          case 66: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.Resource.ResourceManagerLienXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 74: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
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
            CreateTime = input.ReadString();
            break;
          }
          case 18: {
            Id = input.ReadString();
            break;
          }
          case 26: {
            Name = input.ReadString();
            break;
          }
          case 34: {
            Origin = input.ReadString();
            break;
          }
          case 42: {
            Parent = input.ReadString();
            break;
          }
          case 50: {
            Reason = input.ReadString();
            break;
          }
          case 58: {
            restrictions_.AddEntriesFrom(ref input, _repeated_restrictions_codec);
            break;
          }
          case 66: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.Resource.ResourceManagerLienXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 74: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
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
